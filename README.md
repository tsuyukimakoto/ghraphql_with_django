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

Mutations
----

- データの変更定義

- input: mutationのための特殊な型。個別のフィールドではなくてオブジェクト全体を渡したい場合に使う
- Payloads: 標準の型。mutationの出力として。

```
input ActorInput {  
  id: ID
  name: String!
}

input MovieInput {  
  id: ID
  title: String
  actors: [ActorInput]
  year: Int
}
```

```
type ActorPayload {  
  ok: Boolean
  actor: Actor
}

type MoviePayload {  
  ok: Boolean
  movie: Movie
}
```

- ok: payloadによく組み込まれるmetadata

Mutationの定義は

```
type Mutation {  
  createActor(input: ActorInput) : ActorPayload
  createMovie(input: MovieInput) : MoviePayload
  updateActor(id: ID!, input: ActorInput) : ActorPayload
  updateMovie(id: ID!, input: MovieInput) : MoviePayload
}
```

