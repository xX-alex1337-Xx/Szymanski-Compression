def compress(file_name, search_buffer_len = 16, lookahead_buffer_len = 8):
    try:
        # open the file to be compressed
        file = open(file_name, 'rb')
    except:
        print("Error: File not found")
        return
    data = file.read()
    file.close()
    # create a new file to store the compressed data
    new_file = open(file_name + '.lz77', 'at')
    
    # compress the data <j,l> j is the relative index of the first byte of the match, l is the length of the match
    compressed = ''
    sliding_window_len = search_buffer_len + lookahead_buffer_len
    
    for i in data:
        sliding_window = []
        for j in range(sliding_window_len):
            sliding_window.append(data[i+j])
        
        print(sliding_window)
    
    # write the compressed data to the new file and close it
    new_file.write(compressed)
    new_file.close()


compress('test.txt')
