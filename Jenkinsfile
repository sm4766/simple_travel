node {
   // Mark the code checkout 'stage'....
   stage 'Checkout'


   // Checkout code from repository
   checkout scm

   // Run the server
   stage 'Start Server'
   sh ". /etc/simple_travel.env && ./manage.py localhost:8000&"

   stage 'Load Test'
   sh "cd ${PWD}/load_tests && ./post-commit.yml"
}
