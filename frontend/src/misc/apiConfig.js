let baseEndpoint;

const hostname = window && window.location && window.location.hostname;

// Add different endpoints for different hostnames
// Nginx was configured to redirect requests to /api to backend service
baseEndpoint = "UNDEFINED1"

if(process.env.REACT_APP_RUN_ENV == "test"){
    baseEndpoint = 'http://localhost:8081'
}
else if(process.env.REACT_APP_RUN_ENV == "official"){
    baseEndpoint = 'http://localhost:8080'
}

export const ENDPOINT_ROOT = `${baseEndpoint}/api`