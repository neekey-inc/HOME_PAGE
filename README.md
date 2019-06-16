# HOME_PAGE

## Nuxt環境構築

* Project name

  * admin,client,customerの3つを作成した。

* Project description

  * engine,company,user

* Use a custom server framework

  * express

* Choose features to install (Press space to select, a to toggle all, i to invert selection)

* Use a custom UI framework

  * element-ui

* Use a custom test framework

  * jest

* Choose rendering mode

  * Universal

* Author name

  * Takaaki Takada

* Choose a package manager
  
  * npm

1. npx create-nuxt-app projectnameでプロジェクトを作成（これは既にやってあるのでやらないでください）
2. npm install(できない場合はnodeをインストールからやりましょう)
3. npm run dev

## Djang環境構築

1. cd DAICO_ENGINE/api
2. pyenv virtualenv 3.6.5 daico
3. pyenv local daico
4. pip install django==2.1
5. pip install django-rest-framework
6. pip install django-cors-headers
7. pip install sqlalchemy
8. pip install mysqlclient
9. python manage.py runserver

## mysql反映

1. create database homepagedb;でデータベースを作る
