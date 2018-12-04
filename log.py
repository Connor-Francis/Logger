import logging

logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG,
                    format="%(asctime)s – %(levelname)s: %(message)s")

logging.debug("This is a debug")
