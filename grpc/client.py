import grpc
import showcollection_pb2_grpc
import showcollection_pb2
def run():
    # create a channel

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = showcollection_pb2_grpc.ShowCollectionServiceStub(channel)

        print("sends showid")
        request = showcollection_pb2.ShowCollectionRequest(showslug='Sanjay')
        response = stub.SendShowCollection(request)

        print(response.showid)
        print(response.success)


if __name__ == '__main__':
    run()