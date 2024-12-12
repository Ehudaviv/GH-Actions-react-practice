const core = require("@actions/core");
const exec = require("@actions/exec");
const github = require("@actions/github");

function run() {
  core.notice("Deploying to S3");

  const bucket = core.getInput("bucket");
  const distFolder = core.getInput("dist-folder");
  const region = core.getInput("region");

  const s3Uri = `s3://${bucket}`;
  exec.exec(`aws s3 sync ${distFolder} ${s3Uri} --region ${region}`);

  const websiteUrl = `http://${bucket}.s3-website-${region}.amazonaws.com`;
  core.setOutput('url', websiteUrl);
}

run();
