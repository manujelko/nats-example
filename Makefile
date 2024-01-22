.PHONY: nats/network
nats/network:
	docker network create nats-cluster-network

.PHONY: nats/1
nats/1:
	docker run --rm -ti --network nats-cluster-network --name nats1 -p 4222:4222 -p 8222:8222 nats:latest -m 8222 --cluster nats://0.0.0.0:6222 --cluster_name test_cluster

.PHONY: nats/2
nats/2:
	docker run --rm -ti --network nats-cluster-network --name nats2 -p 5222:4222 nats:latest --cluster nats://0.0.0.0:6222 --routes nats-route://nats1:6222 --cluster_name test_cluster

.PHONY: nats/3
nats/3:
	docker run --rm -ti --network nats-cluster-network --name nats3 -p 6222:4222 nats:latest --cluster nats://0.0.0.0:6222 --routes nats-route://nats1:6222 --cluster_name test_cluster
