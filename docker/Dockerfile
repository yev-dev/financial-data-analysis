FROM continuumio/anaconda3

LABEL name="fda" \
summary="financial-data-analysis Python Docker image" \
description="financial-data-analysis Python Docker image" \
maintainer="yevgeniy.yermoshin@db.com"

ENV USER_NAME=fda-user

ENV USER_ID=1000

ARG YUM_DEPS="bzip2 gcc gcc-c++ nmap-ncat git krb5-devel"

ARG DBCONDA_VERSION="2019_07-py37-r351-1.3.4-0"

ARG ARTIFACTORY-USERNAME
ARG ARTIFACTORY—TOKEN
ARG ARTIFACTORY—URL="artifactory.intranet.db.com"

ARG PIP-INDEX_URL="https://${ARTIFACTORY_USERNAME}:${ARTIFACTORY_TOKEN}@${ARTIFACTORY_URL}/artifactory/api/pypi/pypi-all/simple”

ENV APP-NAME="fda"
ENV HOME="/home/${USERNAME}"
ENV DBCONDA_HOME="/opt/dbConda-${DBCONDA—VERSION}"
ENV PATH="${DBCONDA_HOME}/bin:${PATH}"
ENV VENV_HOME="/opt/python/venv"
ENV PATH="$VENV—HOME/bin:$PATH"	J
ENV PYTHONUNBUFFERED=1

RUN useradd -u ${USERID} --shell /bin/bash --gid 0 --create-home --home-dir ${HOME} ${USER_NAME}build

RUN echo "Installing Yum dependencies" && \
yum install ${YUM_DEPS} -y --skip-broken && \
yum clean all && \
rm -rf /var/cache/yum

RUN echo "Downloading dbConda" && \
DBCONDA_URL=”https://${ARTIFACT0RY_URL}/artifactory/dist-public-local/com/db/dbconda/dbConda-${DBC0NDA_VERSIQN}-Linux-x86_64.sh" && \
curl -fsSL -H "X-JFrog-Art-API: ${ARTIFACTORY_TOKEN}" "${DBCONDA_URL}" > /tmp/dbConda.sh && \
NETRC_FILE=${HOME}/.netrc && \
echo "Setting Artifactory token for ${ARTIFACTORY_USERNAME} in ${NETRC_FILE}" && \
echo "machine ${ARTIFACTORY_URL}" >"$NETRC FILE" && \
echo "login ${ARTIFACTORY_USERNAME}" >>"$NETRC_FILE" && \
echo "password ${ARTIFACTORY_TOKEN}" >>"$NETRC_FILE" && \
echo "Installing dbConda" &&\
/bin/bash /tmp/dbConda.sh -bs -p "${DBCONDA_HOME}" && \
echo "Activating Conda" && \
source ${DBCONDA_HOME}/etc/profile.d/conda.sh && \
echo "Configuring Conda" && \
conda config --set channel alias "https://${ARTIFACTORY_URL}/artifactory" && \
conda config --set ssl verify False && \
echo "Cleaning up" && \
rm /tmp/dbConda.sh && \
conda clean -qay && \
rm "${NETRC_FILE}" && \
rm "${HOME}/.condarc"
RUN echo "Setting ownership of home directory" && \
chown -R ${USER_ID}:0 ${HOME} && \
chmod -R 775 ${HOME}

WORKDIR ${HOME}

COPY fda ${HOME}/fda

COPY requirements-docker.txt ${HOME}/requirements.txt

COPY setup.py ${HOME}/setup.py

RUN echo "Creating & activating virtual environment" && \
python -m venv ${VENV HOME} && \
source ${VENV_HOME}/bin/activate && \
echo "Configuring Pip" && \
pip install --trusted-host ${ARTIFACTORY_URL} --index-url ${PIPINDEXURL} --upgrade pip==21.0.1 && \
echo "Installing Pip dependencies" && \
pip install --trusted-host ${ARTIFACTORY_URL} --index-url ${PIPINDEXURL} -r requirements.txt && \
pip install -e .


RUN echo "Creating Jupyter notebook related directories" && \
mkdir -p ${HOME}/notebooks && \
mkdir -p ${HOME}/notebooks/data

RUN echo "Setting up Jupyter password" && \
jupyter notebook --generate-config && \
echo "c.NotebookApp.password='shal;***'"»${home}/.jupyter/jupyternotebookconfig.py

CMD [ "jupyter","lab", "--notebook-dir=notebooks", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root", "--NotebookApp.token=''","--NotebookApp.password=''"]







