import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from deepeval import evaluate
from deepeval.metrics import FaithfulnessMetric, AnswerRelevancyMetric, ContextualPrecisionMetric
from deepeval.test_case import LLMTestCase
from itsupportbot.retrieval_generation import generation
from itsupportbot.ingest import ingestdata
from test_case_eval.test_data import test_cases

def run_deepeval():
    # Load your RAG chain and vector store
    vstore = ingestdata("done")
    chain = generation(vstore)

    # Define metrics
    metrics = [
        FaithfulnessMetric(),
        AnswerRelevancyMetric(),
        ContextualPrecisionMetric()
    ]

    deepeval_cases = []

    # Loop through test cases
    for t in test_cases:
        query = t["input"]
        expected_output = t["expected_output"]

        # Get chatbot response
        actual_output = chain.invoke(query)
        if isinstance(actual_output, dict):
            actual_output = actual_output.get("text", str(actual_output))

        # Retrieve supporting context from your vector store
        try:
            docs = vstore.similarity_search(query, k=3)
            retrieval_context = [doc.page_content for doc in docs]
        except Exception as e:
            print(f"Warning: context retrieval failed for '{query}': {e}")
            retrieval_context = ["No context retrieved"]

        # Build DeepEval test case
        test_case = LLMTestCase(
            input=query,
            expected_output=expected_output,
            actual_output=actual_output,
            retrieval_context=retrieval_context
        )
        deepeval_cases.append(test_case)

    # Run evaluation
    results = evaluate(test_cases=deepeval_cases, metrics=metrics)
    #print(results)
    return results

if __name__=='__main__':
    res = run_deepeval()
    #print(res)

