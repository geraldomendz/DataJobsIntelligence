import base64
import json

def generate_gupy_url(job_id, subdomain="qca"):
    payload = {
        "jobId": int(job_id),
        "source": "gupy_portal"
    }

    encoded = base64.b64encode(
        json.dumps(
            payload,
            separators=(',', ':')
        ).encode()
    ).decode()

    return (
        f"https://{subdomain}.gupy.io/job/"
        f"{encoded}?jobBoardSource=gupy_portal"
    )