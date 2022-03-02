# APIs
Create      POST            /posts          @app.post("/posts")


Read        GET             /posts/:id      @app.get("/posts/[id]")
            GET             /posts          @app.get("/posts")

Update      PUT/PATCH       /posts/:id      @app.put("/posts/{id}")


Delete      DELETE          /posts/:id      @app.delete("/posts/{id}")




## Manual process                       
Make changes to code
Commit changes
Run tests
Build Image
Deploy

## Automated process
Make changes to code       @Continuous integration
|
Commit changes           => Pull source code
                                    |
                            Install Dependencies
                                    |
                            Run Automated Tests     Continuous Delivery
                                    |
                            Build images         => Grab images/code
                                                            |
                                                    Update Production