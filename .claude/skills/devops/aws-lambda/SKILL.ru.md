---
name: aws-lambda
description: "Builds and deploys serverless functions with AWS Lambda, API Gateway, and SAM/CDK. Use for event-driven architectures."
category: devops
tags: [aws-lambda, devops, russian]
models: [sonnet, opus]
version: "1.0"
language: ru
original: aws-lambda
---
# AWS Lambda

> Серверные функции на AWS Lambda, API Gateway и событийные триггеры.

## Быстрый старт
```typescript
import { Handler, APIGatewayProxyEvent, APIGatewayProxyResult } from 'aws-lambda';

export const handler: Handler = async (event: APIGatewayProxyEvent): Promise<APIGatewayProxyResult> => {
  return {
    statusCode: 200,
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      message: 'Hello from Lambda!',
      path: event.path,
      method: event.httpMethod,
    }),
  };
};
```

```yaml
# template.yaml (SAM)
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  HelloFunction:
    Type: AWS::Serverless::Function
    Properties:
      CodeUri: src/
      Handler: index.handler
      Runtime: nodejs20.x
      Events:
        Api:
          Type: Api
          Properties:
            Path: /hello
            Method: GET
```

## Когда использовать
- Событийно-ориентированные serverless API
- Фоновая обработка (ресайз изображений, отправка email)
- Не для длительных процессов (> 15 минут)

## Пошаговые инструкции
1. Установите AWS SAM CLI
2. Создайте SAM-шаблон с Lambda-функциями
3. Напишите Handler-код
4. Деплой: `sam deploy --guided`

## Зависимости
```bash
# Установка AWS SAM CLI
# https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html
npm install aws-lambda @types/aws-lambda
```

## Примеры
Вход: GET /hello → Выход: `{ "message": "Hello from Lambda!" }`

## Ресурсы
- [AWS Lambda Docs](https://docs.aws.amazon.com/lambda/)
- [Examples](./examples/)

## Устранение неполадок
- **Всплески cold start** — не раздувайте зависимости, включите provisioned
  concurrency для горячих путей и выбирайте лёгкие рантаймы (Node/Go).
- **Таймауты на 6s в VPC** — дефолтное время Lambda слишком мало.
  Увеличьте таймаут и проверьте маршруты NAT-шлюза в приватные подсети.
- **SDK отвечает Permission denied** — у execution role нет политик.
  Выдайте least-privilege IAM-политику и повторите запрос без них.
- **`/tmp` переполняется** — 512MB общего хранилища между вызовами.
  Очищайте его в finally-блоке или храните там только мелкие файлы.

## Валидация
1. Функция успешно деплоится
2. Endpoint API Gateway отвечает
3. CloudWatch логи показывают выполнение
