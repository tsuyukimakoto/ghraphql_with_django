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

Queries
----

- 以下はIDからActor、IDからMovie、ないしは絞り込みなしでActorの配列、Movieの配列を取得するQueryかな？

```
type Query {  
  actor(id: ID!): Actor
  movie(id: ID!): Movie
  actors: [Actor]
  movies: [Movie]
}
```