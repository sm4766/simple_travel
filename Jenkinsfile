node {
   // Mark the code checkout 'stage'....
   stage 'Checkout'

   // Checkout code from repository
   checkout scm

   // Mark the code build 'stage'....
   stage 'Load Test'
   // Run the maven build
   sh "cd load_tests && ./post-commit.yml"
}
