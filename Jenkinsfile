node {
   // Mark the code checkout 'stage'....
   stage 'Checkout'


   // Checkout code from repository
   checkout scm

   // Run the server
   stage 'Start Server'
   sh "./manage.py localhost:8000&"

   // Mark the code build 'stage'....
   stage 'Load Test'
   // Run load test
   sh "cd ${PWD}/load_tests && ./post-commit.yml"
}
