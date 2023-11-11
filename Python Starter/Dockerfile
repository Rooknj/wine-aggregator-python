FROM docker.intuit.com/docker-rmt/python:3.11-slim-bullseye as base
# USER root needed for build, since CPD does not allow root user for gold images.
# intermediate containers will be discarded at final stage, runtime image will be executed with non root user
USER root

# Download latest Contrast dependency for SSDLC control AS019.4
FROM docker.intuit.com/docker-rmt/curlimages/curl:8.00.1 as contrast
RUN curl -o /tmp/contrast.tar.gz https://artifact.intuit.com/artifactory/generic-local/dev/security/ssdlc/contrast/python/latest/contrast-python-agent.tar.gz

FROM base as venv
RUN mkdir /virtualenvs
WORKDIR /runtime
RUN mkdir -p /opt/poetry \
  && python -m venv /opt/poetry/venv \
  && /opt/poetry/venv/bin/python -m pip install -U pip setuptools \
  && /opt/poetry/venv/bin/python -m pip install poetry==1.4.2
COPY pyproject.toml poetry.lock ./
ENV PATH=/opt/poetry/venv/bin:$PATH
RUN poetry --version \
  && poetry config virtualenvs.in-project true --local
# poetry.lock must exist, but empty file means rebuild it
RUN [ -s poetry.lock ] \
  || (echo "WARNING: poetry.lock not found, rebuilding..." \
  && rm -f poetry.lock \
  && poetry lock \
  )
# This is done to elimiate ValueError: Package('setuptools', '67.8.0') is not in list due to
#   Connection pool is full, discarding connection: artifact.intuit.com. Connection pool size: 10
RUN poetry config installer.max-workers 10
RUN poetry install --no-root --without dev,test


FROM base as build

WORKDIR /app 
# The following ARG and 2 LABEL are used by Jenkinsfile command
# to identify this intermediate container, for extraction of
# code coverage and other reported values.
ARG build
ARG GIT_BRANCH
ARG GIT_COMMIT
ARG DOCKER_TAGS=latest
# ARG JIRA_PROJECT=https://jira.intuit.com/projects/<CHANGE_ME>
ARG DOCKER_IMAGE_NAME=docker.intuit.com/qbshared-integrations/qbaa-genai-plugin/service/qbaa-genai-plugin:${DOCKER_TAGS}
ARG SERVICE_LINK=https://devportal.intuit.com/app/dp/resource/3029814242517068521

LABEL maintainer=rafael_pinerosrhon@intuit.com \
  app=qbaa-genai-plugin \
  app-scope=runtime \
  build=${build}

COPY --from=contrast /tmp/contrast.tar.gz /app/contrast/pythonagent/
COPY contrast_security.yaml /home/appuser/contrast_security.yaml
COPY package/post_harden.sh /home/appuser/post_harden.sh
COPY package/entry.sh /app/entry.sh

COPY app ./
COPY --from=venv /runtime/.venv /runtime/.venv/

RUN chmod +x /home/appuser/post_harden.sh \
  && chmod +x /app/entry.sh \
  && mkdir /app/tmp \
  && useradd -ms /bin/bash appuser \
  && chown appuser:appuser /app -R \
  && chown appuser:appuser /runtime -R \
  && /home/appuser/post_harden.sh

USER appuser

CMD ["/bin/bash", "/app/entry.sh"]