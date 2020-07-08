doc = '''
mediaType: application/json
protocols: [ HTTP,HTTPS] 
securitySchemes:
    JWT:
        description: We support JWT for authenticating all API requests.
        type: JWT
        describedBy:
            headers:
                Authorization:
                    type: string
            queryParameters:
                access_token:
                    type: string
            responses:
                401:
        settings:
            signatures: ['HMAC-SHA256']
types:
  Auth:
    type: object
    discriminator: token
    properties:
      token: string
  User:
    type: object
    discriminator: user_id
    properties:
        user_id: integer
        name:
            type: string
            maxLength: 50
        email: 
            type: string
            maxLength: 254
        password : 
            type: string
            maxLength: 50
        last_login : datetime-only
        group_id: integer
    example:
        user_id: 2
        name: emmanuel
        email: manolo@bol.com
        password : 79799
        last_login : 2020-07-01T10:10:10
        group_id: 2
  Event:  
    type: object
    discriminator: event_id
    properties:
        event_id: integer
        level: 
            type: string
            maxLength: 20
        payload: string
        shelve: boolean
        date: datetime-only
        agent_id: integer
    example:
        event_id: 12
        level: bug
        payload: bug
        shelve: false
        date: 2020-07-01T10:10:10

  Group:
    type: object
    discriminator: group_id
    properties:
        group_id : integer
        name : 
            type: string
            maxLength: 20
    example:
        group_id: 4
        name: Data

  Agent:
    type: object
    discriminator: agent_id
    properties:
        agent_id : integer
        user_id: integer
        name :
            type: string
            maxLength: 50
        address : 
            type: string
            maxLength: 39
        status : boolean
        environment : 
            type: string
            maxLength: 20
        version :
            type: string
            maxLength: 5
        user_id : integer
    example:
        event_id: integer
        level: 
            type: string
            maxLength: 20
        payload: string
        shelve: boolean
        date: datetime-only
        agent_id: integer
    example:
        event_id: 12
        level: bug
        payload: bug
        shelve: false
        date: 2020-07-01T10:10:10

  Group:
    type: object
    discriminator: group_id
    properties:
        group_id : integer
        name : 
            type: string
            maxLength: 20
    example:
        group_id: 4
        name: Data

  Agent:
    type: object
    discriminator: agent_id
    properties:
        agent_id : 6
        user_id: 2
        name : carlos
        address : manolo
        status : false
        environment : Linux
        version : 1.0
        user_id : 2
/auth/token:
    post: 
        body: 
            application/json:
                properties:
        responses:
            201:
                body: 
                    application/json:
                        Auth[]
            400:
                body: 
                    applicatioon/json:
                        {"error":"Bad Request"}

    
/agents:
    description: A set of agents.
    post:
        description: create an agent. 
        securedBy:
            [JWT]
        body:
            type: 
                application/json:
                    propreties:
                    example: |
                        {"user_id": 0,
                        "name": "teste",
                        "status": true,
                        "environment": "teste",
                        "version": "v1",
                        "address": "12.33.55.66"
                        }    
        responses:
            201:
                body: Agent
            401:
                body:
                    appplication/json: |
                        {"error": "Authorization Required"}
            404:
                body:
                    application/json: |
                        {"error": "Bad Request"}

    get:
        description: see an agent list. 
        securedBy:
            [JWT]
        responses: 
            200:
                body: Agent[]
            401:
                body:
                    application/json: |
                        {"error": "Authorization Required"}
            404:
                body:
                    application/json: |
                        {"error": "Bad Request"}
                        

    
    /{id}:
        description: A agent based on id.
        put:
            description: create an agent based on the id. 
            securedBy:
                [JWT] 
            responses:
                200:
                    body: Agent
                401:
                    body:
                        application/json: |
                            {"error": "Authorization Required"}
                404:
                    body:
                        application/json: |
                            {"error": "Bad Request"}
                            
        get:
            description: see an Agent
            securedBy:
                [JWT]
            responses:
                200:
                    body: Agent
                401:
                    body:
                        application/json: |
                            {"error": "Authorization Required"}
                404:
                    body:
                        application/json: |
                            {"error": "Bad request"}
                
        delete:
            description: delete
            securedBy:
                [JWT]
            responses:
                200:
                    body:
                        application/json:
                            {"mensage":"Ok"}
                401:
                    body:
                        application/json: |
                            {"error": "Authorization Required"}
                404:
                    body:
                        application/json: |
                            {"error": "Bad Request"}
                            


    /{id}/events:
        description: A set of events.
        put:
            description: create an event. 
            securedBy:
                [JWT]
            body:
                type: Event
            responses:
                200:
                    body:
                        application/json: 
                            type: Event
                401:
                    body:
                        application/json: |
                            {"error": "Authorization Required"}
                404:
                    body:
                        application/json: |
                            {"error": "Bad Request"}
                            

        get:
            description: see an event. 
            securedBy:
                [JWT]
            responses:
                200:
                    body: 
                        application/json:
                            type: Event[]
                401:
                    body:
                        application/json: |
                            {"error": "Authorization Required"}
                404:
                    body:
                        application/json: |
                            {"error": "Bad Request"}
                            
        delete:
            description: delete an event. 
            securedBy:
                [JWT]
            responses:
                200:
                    body:
                        application/json:
                            {"mensage":"Ok"}
                401:
                    body:
                        application/json: |
                            {"error": "Authorization Required"}
                404:
                    body:
                        application/json:
                            
        /{id}:
            description: An event.
            put:
                description: create an event. 
                securedBy: 
                    [JWT] 
                body:
                    application/json:
                        type: Event
                responses:
                    200:
                        body: 
                            type:
                                application/json:
                                    Event
                    401:
                        body:
                            type:
                                application/json: |
                                    {"error": "Authorization Required"}    
                    404:
                        body:
                            type: 
                                application/json: |
                                    {"error": "Bad Request"}
                                    
            get:
                description: see an event. 
                securedBy:
                    [JWT]
                responses:
                    200:
                        body:
                            type:
                                application/json:
                                    Event
                    401:
                        body:
                            type:
                                application/json:|
                    404:
                        body:
                            application/json: |
                                {"error": "Bad Request"}
                                    
            delete:
                description: delete an event. 
                securedBy:
                    [JWT]
                responses:
                    200:
                        body:
                            application/json:
                                {"mensage":"Ok"}
                    401:
                        body:
                            application/json: |
                                {"error": "Authorization Required"}
                                
                    404:
                        body:    
                            application/json: |
                                {"error": "Bad Request"}
                                
/users:
    description: A set of users.
    post:
        description: create an user. 
        securedBy:
            [JWT] 
        body:
            type: User
        responses:
            201:
                body:
                    application/json:
                        User 
            401:
                body:
                    application/json: |
                        {"error": "Authorization Required"}
            404:
                body:
                    application/json: |
                        {"error": "Bad Request"}
                         
    get:
        description: get a set of user. 
        securedBy:
            [JWT]
        responses:
            200:
                body:
                    type:
                        application/json:
                            User[]
            401:
                body:
                    type:
                        application/json: |
                            {"error": "Authorization Required"}
            404:
                body:
                    type:
                        application/json: |
                            {"error": "Bad Request"}
                         

    /{id}:
        description: An user based on id.
        put:
            description: create an user. 
            securedBy: 
                [JWT] 
            body:
                application/json:
                    type: User
            responses:
                200:
                    body:
                        application/json:
                            User
                401:
                    body:
                        application/json: |
                            {"error": "Authorization Required"}
                404:
                    body:
                        application/json: |
                            {"error": "Bad Request"}
                            
        get:
            description: see an user. 
            securedBy:
                [JWT]
            responses:
                200:
                    body:
                        application/json:
                            User
                401:
                    body:
                        application/json: |
                            {"error": "Authorization Required"}
                404:
                    body:
                        application/json: |
                            {"error": "Bad Request"}
                            
        delete:
            description: delete an user. 
            securedBy:
                [JWT]
            responses:
                200:
                    body:
                        application/json:
                            {"mensage":"Ok"}

                401:
                    body:
                        application/json: |
                            {"error": "Authorization Required"}
                            
                404:
                    body:
                        application/json: |
                            {"error": "Bad Request"}
                            
/groups:
    description: A set of group.
    post:
        description: create an group. 
        securedBy:
            [JWT]
        body:
            type: Group
        responses:
            201:
                body:
                    application/json:
                            {"mensage":"Ok"}
            401:
                body:
                    application/json: |
                        {"error": "Authorization Required"}
            404:
                body:
                    application/json: |
                        {"error": "Bad Request"}
                        
    get:
        description: see an group. 
        securedBy:
            [JWT]
        responses:
            200:
                body:
                    application/json:
                        Group[]
            401:
                body:
                    application/json: |
                        {"error": "Authorization Required"}
            404:
                body:
                    application/json: |
                        {"error": "Bad Request"}
                        
    /{id}:
        description: A set of movies.
        put:
            description: create an group id. 
            securedBy:
                [JWT] 
            responses:
                200:
                    body:  
                        application/json:
                            Group
                401:
                    body:
                        application/json: |
                            {"error": "Authorization Required"}
                404:
                    body:
                        application/json: |
                            {"error": "Bad Request"}
                            
        get:
            description: see a group. 
            securedBy:
                [JWT]
            responses:
                200:
                    body:
                        application/json:
                            Group
                401:
                    body:
                        application/json: |
                            {"error": "Authorization Required"}
                404:
                    body:
                        application/json: |
                            {"error": "Bad Request"}
                                
        delete:
            description: delete a group. 
            securedBY:
                [JWT]
            responses:
                200:
                    body:
                        application/json:
                            {"mensage":"Ok"}

                401:
                    body:
                        application/json: |
                            type: Error
                            
                404:
                    body:
                        application/json: |
                            {"error": "Bad Request"}
                            
'''     
