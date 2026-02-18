const core = require("@actions/core");
const github = require("@actions/github");

function run() {
  core.notice("Starting deployment to AWS S3...");

  setTimeout(() => {
    core.notice("Deployment to AWS S3 completed successfully!");
  }, 2000);
}

run();
