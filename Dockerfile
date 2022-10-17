FROM python:3.8

COPY ./ /home/SeleniumTestFramework/

# Adding trusting keys to apt for repositories
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -

# Adding Google Chrome to the repositories
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'

# Updating apt to see and install Google Chrome
RUN apt-get -y update

# Magic happens
RUN apt-get install -y google-chrome-stable


RUN apt-get -y install allure

RUN pip install pytest

RUN pip install selenium

RUN pip install allure-pytest

RUN pip install webdriver_manager

RUN pip install allure-python-commons












CMD ["sleep","3000"]