import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from chalice import Chalice
from app.main import app as fastapi_app
from mangum import Mangum

chalice_app = Chalice(app_name='sbmt-notify-svc')
handler = Mangum(fastapi_app)

@app.lambda_function()
def main(event, context):
    return handler(event, context)
