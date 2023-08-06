# Create your views here.
import logging
import json
import jsonschema
from pathlib import Path

logger = logging.getLogger("info_logs")
logger_error = logging.getLogger('error_logs')


def schema_validation(data, path):
    """Function for validating Json Schema functionality."""
    try:
        flag = 0
        schema = load(path)
        logger.info(schema)
        data = data.get_json()
        v = jsonschema.Draft4Validator(schema)
        logger.info(v)
        logger.info('v: come here 36')
        errors = sorted(v.iter_errors(data), key=lambda e: e.path)
        logger.info('errors: come here 39')
        for error in errors:
            logger.info('json validation failed')
            flag = 452
            logger.info('come here 49')
            output_json = dict(zip(['Status', 'Message'], [flag, error.message]))
            return output_json
        logger.info('schema validation done')
        output_json = dict(zip(['Status', 'Message'], [flag, 'schema validation done']))
        return output_json
    except Exception as ex:
        logger_error.error(f"Exception Encountered Exception is : {ex}", exc_info=1)
        output_json = dict(zip(['Status', 'Message'], [500, f"Exception encountered: {ex}"]))
        return output_json


def load(schema_path):
    """
    :param schema_path:
    :return:
    """
    schema = Path(schema_path)

    with schema.open() as f:
        return json.load(f)
