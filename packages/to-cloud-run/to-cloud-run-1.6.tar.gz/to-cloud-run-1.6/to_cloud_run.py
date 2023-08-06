#!/usr/bin/env python
from argparse import ArgumentParser
from os import getenv, system, path, getcwd

from dotenv import load_dotenv


def create_dockerfile():
    if not path.exists('./Dockerfile'):
        dockerfile = """
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
"""
        with open('./Dockerfile', 'w') as f:
            f.write(dockerfile)


def build_docker_image(service_name, platform='linux/amd64', tag='1.9.0'):
    create_dockerfile()
    system(f'docker build --platform {platform} -t {service_name} .')
    image_repo = f'gcr.io/{getenv("GCP_PROJECT_ID")}/{service_name}:{tag}'
    system(f'docker tag {service_name} {image_repo}')
    system(f'docker push {image_repo}')
    return image_repo


def deploy_cloud_run(service_name, image_repo, service_account, region='us-central1', cpu=0.08, memory='128Mi',
                     max_instances=1, port=8000):
    system(f'gcloud config set run/region {region}')
    system(f'gcloud run deploy {service_name} '
           f'--image={image_repo} '
           f'--allow-unauthenticated '
           f'--port={port} '
           f'--service-account={service_account} '
           f'--concurrency=1 '
           f'--cpu={cpu} '
           f'--memory={memory} '
           f'--max-instances={max_instances} '
           f'--region={region} '
           f'--project={getenv("GCP_PROJECT_ID")}')


def usage():
    print('''Suggest create requirements.txt at folder root:
uvicorn
fastapi
starlette
pydantic
jinja2

Please put your main fastapi files into folder root ./app.py
    ''')


def main():
    usage()
    load_dotenv(getcwd() + "/.env")
    if not getenv('GCP_PROJECT_ID'):
        print('Error: GCP_PROJECT_ID is not set in the environment or .env file.')
        return
    if not getenv('GCP_SERVICE_ACCOUNT'):
        print('Error: GCP_SERVICE_ACCOUNT is not set in the environment or .env file.')
        return

    parser = ArgumentParser(description='Deploy a service to GCP Cloud Run')
    arg = parser.add_argument
    arg('-n', '--service-name', required=True, help='Service name')
    arg('-p', '--platform', default='linux/amd64', help='Docker build platform')
    arg('-t', '--image-tag', required=True, help='Docker image tag')
    arg('-s', '--service-account', default=getenv('GCP_SERVICE_ACCOUNT'),
        help='GCP service account email')
    arg('-c', '--cpu', default=0.08, type=float, help='Cloud Run CPU allocation')
    arg('-m', '--memory', default='128Mi', help='Cloud Run memory allocation')
    arg('-i', '--max-instances', default=1, type=int, help='Cloud Run maximum instance count')
    arg('-r', '--region', default='us-central1', help='Cloud Run region')
    arg('-o', '--port', default=8000, type=int, help='Container port')

    args = parser.parse_args()

    image_tag = args.image_tag
    service_name = args.service_name
    image_repo = build_docker_image(service_name, platform=args.platform, tag=image_tag)
    deploy_cloud_run(service_name, image_repo=image_repo, service_account=args.service_account, region=args.region,
                     cpu=args.cpu, memory=args.memory, max_instances=args.max_instances,
                     port=args.port)


if __name__ == '__main__':
    main()
