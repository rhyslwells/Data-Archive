#### REST API
- REST stands for Representational State Transfer.
- It is a ==standardized== software architecture style used for API communication between a client and a server.

**Benefits of REST APIs:**
1. **Simplicity and Standardization:**
   - Data formatting and request structuring are standardized and widely adopted.
2. **Scalability and Statelessness:**
   - Easily modifiable as service complexity grows without tracking data states across client and server.
3. **High Performance:**
   - Supports ==caching==, maintaining high performance even as complexity increases.

**Main Building Blocks:**
1. **==Request==:**
   - Actions (==[[CRUD]]==): Create (POST), Read (GET), Update (PUT), Delete (DELETE).
   - Components: Operation (==HTTP method==), Endpoint, Parameters/Body, Headers.
2. **Response:**
   - Typically in [[JSON]] format.

**REST API Example:** 
ice cream shop inteacting with cloud database.
- Endpoint example: "icecream.com/api/flavors"
  - "api" indicates the API portion.
  - "flavors" refers to the ==resource== being accessed or modified.

**Real-world Examples:**
1. **Get Flavors:**
   - Operation: ==GET==
   - Endpoint: "/api/flavors"
   - Response: Array of flavor resources.
2. **Update Flavor:**
   - Operation: ==PUT==
   - Endpoint: "/api/flavors/1"
   - Body: New flavor data.
   - Response: Confirmation of update.
3. **Create New Flavor:**
   - Operation: ==POST==
   - Endpoint: "/api/flavors"
   - Body: New flavor data.
   - Response: Confirmation of creation.