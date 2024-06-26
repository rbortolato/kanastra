import logging

from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException
from fastapi import Request, HTTPException

async def handle_exceptions(request: Request, call_next):
    try:
        response = await call_next(request)
        return response
    except AssertionError as ass:
        logging.warning(str(ass))
        return JSONResponse(status_code=400, content={"msg": str(ass)})
    except HTTPException as http:
        logging.warning(str(http))
        return JSONResponse(status_code=422, content=http.detail)
    except Exception as exp:
        logging.error(str(exp))
        return JSONResponse(status_code=500, content={"msg": "Houve um erro no sistema, tente novamente mais tarde"})
