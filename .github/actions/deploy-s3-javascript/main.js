const core = require("@actions/core");
// const github = require("@actions/github");
const exec = require("@actions/exec");

function run() {
  // 1) Get input parameters
  core.notice("Obtaining AWS S3 Parameters...");
  const s3BucketName = core.getInput("s3_bucket_name", { required: true });
  const s3Region = core.getInput("s3_region", { required: true });
  const distFolder = core.getInput("dist-folder", { required: true });

  core.notice("Starting deployment to AWS S3...");

  // 2) Upload files
  const s3Uri = `s3://${s3BucketName}`;
  exec.exec(`aws s3 sync ${distFolder} ${s3Uri} --region ${s3Region}`);

  setTimeout(() => {
    core.notice("Deployment to AWS S3 completed successfully!");
  }, 2000);
}

run();
