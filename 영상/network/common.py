import struct, cv2, pickle

BUF_SIZE = 1024

def image_unpack(client, data_buffer):
    data_size = struct.calcsize("L")

    while len(data_buffer) < data_size:
        data_buffer += client.recv(BUF_SIZE)

    packed_data_size = data_buffer[:data_size]
    data_buffer = data_buffer[data_size:]
    frame_size = struct.unpack(">L", packed_data_size)[0]

    while len(data_buffer) < frame_size:
        data_buffer += client.recv(BUF_SIZE)

    frame_data = data_buffer[:frame_size]
    data_buffer = data_buffer[frame_size:]

    frame = pickle.loads(frame_data)
    print(f"수신 프레임 크기 : {len(frame)} bytes")
    frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)

    return frame, data_buffer

def image_pack(frame):
    retval, frame = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 90])
    frame = pickle.dumps(frame)

    print(f"전송 프레임 크기 : {len(frame)} bytes")

    return struct.pack(">L", len(frame)) + frame