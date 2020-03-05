from . import main
import logging

watcherAPI = main.PySocialWatcher
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    watcherAPI.load_credentials_file("credentials.csv")
    # watcherAPI.check_tokens_account_valid()
    watcherAPI.run_data_collection("./input_examples/proof_of_concept.json")

