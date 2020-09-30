import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(filename)s [LINE:%(lineno)-10d] # %(levelname)-8s [%(asctime)s] %(message)s"
)

try:
    logging.info("Working")
    logging.warning("Tolic the best)")
    logging.debug("Catching fleas :)   Flea is a very small :o)")
    logging.info("print after logging...")
    exc = Exception('Bebebe', 'Lalala')
    raise exc
except Exception:
    logging.exception("E R R O R ! ! !")
finally:
    logging.info("print finally...")