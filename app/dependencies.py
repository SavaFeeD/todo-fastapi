from starlette.responses import JSONResponse
from fastapi import HTTPException


def response(status, result=None, error=None):
    if error is not None:
        raise HTTPException(status_code=status, detail=error)
    else:
        return JSONResponse({
            "result": result,
            "status": status
        })
