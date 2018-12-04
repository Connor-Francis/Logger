import logging
import coloredlogs

fmt = "%(asctime)s – %(levelname)s: %(message)s"
fieldStyles = {'asctime':{'color':'green'}, 'levelname':{'color':'blue'},'message':{'color':'red'}}


logging.basicConfig(filemode='w', level=logging.INFO,
                    format=fmt)

logger = logging.getLogger(__name__)
coloredlogs.install(level='INFO',logger=logger,fmt=fmt,field_styles=fieldStyles)

logging.info("This is info")