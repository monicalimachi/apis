Create      POST            /posts          @app.post("/posts")


Read        GET             /posts/:id      @app.get("/posts/[id]")
            GET             /posts          @app.get("/posts")

Update      PUT/PATCH       /posts/:id      @app.put("/posts/{id}")


Delete      DELETE          /posts/:id      @app.delete("/posts/{id}")

