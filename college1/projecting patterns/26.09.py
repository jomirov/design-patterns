class Transport:
    def deliverOn(self) -> str:
        pass

class TransportCreator:

    def create_transport(self):
        pass

    def introduce_transport(self):
        transport = self.create_transport()
        return f"Я создал трансопрт, и оно доставляет товары через: {transport.deliverOn()}"


class Truck(Transport):
    def deliverOn(self):
        return "Road"

class Plane(Transport):
    def deliverOn(self):
        return "Air/Sky"

class TruckCreator(TransportCreator):
    def create_transport(self):
        return Truck()

class PlaneCreator(TransportCreator):
    def create_transport(self):
        return Plane()

def client_code(creator: TransportCreator):
    print(creator.introduce_transport())

if __name__ == "__main__":
    print("Создание самолета")
    client_code(PlaneCreator())

    print("Создание truck")
    client_code(TruckCreator())