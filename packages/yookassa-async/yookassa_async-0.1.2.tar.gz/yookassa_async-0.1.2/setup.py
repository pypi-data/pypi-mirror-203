# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['yookassa',
 'yookassa.domain',
 'yookassa.domain.common',
 'yookassa.domain.exceptions',
 'yookassa.domain.models',
 'yookassa.domain.models.confirmation',
 'yookassa.domain.models.confirmation.request',
 'yookassa.domain.models.confirmation.response',
 'yookassa.domain.models.payment_data',
 'yookassa.domain.models.payment_data.request',
 'yookassa.domain.models.payment_data.response',
 'yookassa.domain.models.payout_data',
 'yookassa.domain.models.payout_data.request',
 'yookassa.domain.models.payout_data.response',
 'yookassa.domain.notification',
 'yookassa.domain.request',
 'yookassa.domain.response']

package_data = \
{'': ['*']}

install_requires = \
['deprecated>=1.2.13,<2.0.0',
 'distro>=1.8.0,<2.0.0',
 'httpx>=0.24.0,<0.25.0',
 'netaddr>=0.8.0,<0.9.0',
 'requests>=2.28.2,<3.0.0']

setup_kwargs = {
    'name': 'yookassa-async',
    'version': '0.1.2',
    'description': 'Based on work of https://github.com/tonchik-tm and main yookassa package',
    'long_description': "# YooKassa ASync API Python Client Library\n\n[![Build Status](https://travis-ci.org/yoomoney/yookassa-sdk-python.svg?branch=master)](https://travis-ci.org/yoomoney/yookassa-sdk-python)\n[![Latest Stable Version](https://img.shields.io/pypi/v/yookassa.svg)](https://pypi.org/project/yookassa/)\n[![Total Downloads](https://img.shields.io/pypi/dm/yookassa.svg)](https://pypi.org/project/yookassa/)\n[![License](https://img.shields.io/pypi/l/yookassa.svg)](https://git.yoomoney.ru/projects/SDK/repos/yookassa-sdk-python)\n\nRussian | [English](README.en.md)\n\nКлиент для работы с платежами по [API ЮKassa](https://yookassa.ru/developers/api)\nПодходит тем, у кого способ подключения к ЮKassa называется API.\n\nАсинхронная версия.\n\n## Требования\n\n1. Python >=3.7\n2. pip\n\n## Установка\n### C помощью pip\n\n1. Установите pip.\n2. В консоли выполните команду\n```bash\npip install --upgrade yookassa\n```\n\n### С помощью easy_install\n1. Установите easy_install.\n2. В консоли выполните команду\n```bash\neasy_install --upgrade yookassa\n```\n\n### Вручную\n\n1. В консоли выполните команды:\n```bash\nwget https://pypi.python.org/packages/5a/be/5eafdfb14aa6f32107e9feb6514ca1ad3fe56f8e5ee59d20693b32f7e79f/yookassa-1.0.0.tar.gz#md5=46595279b5578fd82a199bfd4cd51db2\ntar zxf yookassa-1.0.0.tar.gz\ncd yookassa-1.0.0\npython setup.py install\n```\n\n## Начало работы\n\n1. Импортируйте модуль\n```python\nimport yookassa\n```\n2. Установите данные для конфигурации\n```python\nfrom yookassa import Configuration\n\nConfiguration.configure('<Идентификатор магазина>', '<Секретный ключ>')\n```\n\nили\n\n```python\nfrom yookassa import Configuration\n\nConfiguration.account_id = '<Идентификатор магазина>'\nConfiguration.secret_key = '<Секретный ключ>'\n```\n\nили через oauth\n\n```python\nfrom yookassa import Configuration\n\nConfiguration.configure_auth_token('<Oauth Token>')\n```\n\nЕсли вы согласны участвовать в развитии SDK, вы можете передать данные о вашем фреймворке, cms или модуле:\n```python\nfrom yookassa import Configuration\nfrom yookassa.domain.common.user_agent import Version\n\nConfiguration.configure('<Идентификатор магазина>', '<Секретный ключ>')\nConfiguration.configure_user_agent(\n    framework=Version('Django', '2.2.3'),\n    cms=Version('Wagtail', '2.6.2'),\n    module=Version('Y.CMS', '0.0.1')\n)\n```\n\n3. Вызовите нужный метод API. [Подробнее в документации к API ЮKassa](https://yookassa.ru/developers/api)\n\n## Примеры использования SDK\n\n#### [Настройки SDK API ЮKassa](./docs/examples/01-configuration.md)\n* [Аутентификация](./docs/examples/01-configuration.md#Аутентификация)\n* [Статистические данные об используемом окружении](./docs/examples/01-configuration.md#Статистические-данные-об-используемом-окружении)\n* [Получение информации о магазине](./docs/examples/01-configuration.md#Получение-информации-о-магазине)\n* [Работа с Webhook](./docs/examples/01-configuration.md#Работа-с-Webhook)\n* [Входящие уведомления](./docs/examples/01-configuration.md#Входящие-уведомления)\n\n#### [Работа с платежами](./docs/examples/02-payments.md)\n* [Запрос на создание платежа](./docs/examples/02-payments.md#Запрос-на-создание-платежа)\n* [Запрос на создание платежа через билдер](./docs/examples/02-payments.md#Запрос-на-создание-платежа-через-билдер)\n* [Запрос на частичное подтверждение платежа](./docs/examples/02-payments.md#Запрос-на-частичное-подтверждение-платежа)\n* [Запрос на отмену незавершенного платежа](./docs/examples/02-payments.md#Запрос-на-отмену-незавершенного-платежа)\n* [Получить информацию о платеже](./docs/examples/02-payments.md#Получить-информацию-о-платеже)\n* [Получить список платежей с фильтрацией](./docs/examples/02-payments.md#Получить-список-платежей-с-фильтрацией)\n\n#### [Работа с возвратами](./docs/examples/03-refunds.md)\n* [Запрос на создание возврата](./docs/examples/03-refunds.md#Запрос-на-создание-возврата)\n* [Запрос на создание возврата через билдер](./docs/examples/03-refunds.md#Запрос-на-создание-возврата-через-билдер)\n* [Получить информацию о возврате](./docs/examples/03-refunds.md#Получить-информацию-о-возврате)\n* [Получить список возвратов с фильтрацией](./docs/examples/03-refunds.md#Получить-список-возвратов-с-фильтрацией)\n\n#### [Работа с чеками](./docs/examples/04-receipts.md)\n* [Запрос на создание чека](./docs/examples/04-receipts.md#Запрос-на-создание-чека)\n* [Запрос на создание чека через билдер](./docs/examples/04-receipts.md#Запрос-на-создание-чека-через-билдер)\n* [Получить информацию о чеке](./docs/examples/04-receipts.md#Получить-информацию-о-чеке)\n* [Получить список чеков с фильтрацией](./docs/examples/04-receipts.md#Получить-список-чеков-с-фильтрацией)\n",
    'author': 'Илья Снимщиков',
    'author_email': 'igsnimschikov@edu.hse.ru',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
