const core = require('@actions/core');
const exec  = require('@actions/exec');
const github = require('@actions/github');

function run() {
  core.notice('Deploying to S3');
}

run();