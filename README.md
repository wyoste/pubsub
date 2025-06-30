# pubsub
mis 6v99 oroject to create a pubsub pipeline

## Clone Repo
git clone https://github.com/wyoste/pubsub.git

## delete repo to update and re-clone 
cd
rm -rf pubsub

## test pubsub subscription pulling messages:
gcloud pubsub subscriptions pull demographics --limit=5 --auto-ack

