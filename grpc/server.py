import grpc
import time
import showcollection_pb2_grpc
import showcollection_pb2
from concurrent import futures

class ShowCollectionService(showcollection_pb2_grpc.ShowCollectionServiceServicer):
    def SendShowCollection(self, request, context):
        
        print(f"Got the showslug {request.showslug}")
        return showcollection_pb2.ShowCollectionResponse(showid="1",success=True)

def serve():
    # Create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=3))
    showcollection_pb2_grpc.add_ShowCollectionServiceServicer_to_server(ShowCollectionService(), server)

    server.add_insecure_port('[::]:50051')
    server.start()

    print("server started on port 50051")

    try:
        while True:
            time.sleep(64000)
    except KeyboardInterrupt:
        server.stop(0)
        print("Server stopped")

if __name__ == '__main__':
    serve() 
