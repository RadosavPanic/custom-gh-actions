const core = require("@actions/core");
// const github = require("@actions/github");
const exec = require("@actions/exec");

function run() {
  // 1) Get input parameters
  core.notice("Obtaining AWS S3 Parameters...");
  const s3BucketName = core.getInput("S3_BUCKET_NAME", { required: true });
  const s3Region = core.getInput("S3_REGION", { required: true });
  const distFolder = core.getInput("DIST_FOLDER", { required: true });

  core.notice("Starting deployment to AWS S3...");

  // 2) Upload files
  const s3Uri = `s3://${s3BucketName}`;
  exec.exec(`aws s3 sync ${distFolder} ${s3Uri} --region ${s3Region}`);

  setTimeout(() => {
    core.notice("Deployment to AWS S3 completed successfully!");
  }, 2000);
}

run();
