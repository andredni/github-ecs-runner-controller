import time
import logging
from github_api import get_org_runners, register_new_runner, delete_org_runner
from config import CHECK_INTERVAL, LOG_LEVEL

logging.basicConfig(level=getattr(logging, LOG_LEVEL), format='%(asctime)s %(levelname)-6s %(message)s')

def scale_up():

    # if is_runner_token_avaibale():
    #     pass
    # else:
    #     token = register_new_runner()


def scale_down():
    pass


def main():
    logging.info(f"GitHub controller is started.")
    while True:
        try:
            logging.info(f"Currently running Github Runners are checked.")

            runners_info, runners = get_org_runners()
            logging.info(f"No runners were found.") if len(runners_info) == 0 else logging.info("".join([f"{key}: {value} " for key, value in runners_info.items()]))

            if len(runners_info) == 0 or 'online' not in runners_info or runners_info['online'] < 2:
                logging.info(f"There are not enough runners in online status! It is now scaled up.")
                # scale_up()
                register_new_runner()

            elif 'online' in runners_info and runners_info['online'] > 2:
                logging.info(f"There are too many runners. It is now scaled down.")
                # scale_down()

            logging.info(f"Next runner check in {CHECK_INTERVAL} seconds")
            time.sleep(CHECK_INTERVAL)

        except Exception as e:
            logging.error(f"Error in main loop: {e}")
            time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()

