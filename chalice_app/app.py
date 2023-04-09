import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from chalice import Chalice
from app.main import app
from mangum import Mangum

chalice_app = Chalice(app_name='')
handler = Mangum(app)

@app.lambda_function()
def main(event, context):
    return handler(event, context)

