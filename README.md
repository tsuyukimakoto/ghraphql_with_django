# ghraphql-with-django
https://stackabuse.com/building-a-graphql-api-with-django/#disqus_thread

Types
----

- ID: ユニークな識別子（Stringとしてシリアライズされる
- エクスクラメーションマーク: 必須
- listは[]（square brackets）でくくる

```
type <型名> {
  <属性名>: <型>(!)
}
```

```
type Actor {  
  id: ID!
  name: String!
}
```
