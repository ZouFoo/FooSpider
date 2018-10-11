import multiprocessing




if __name__ == "__main__":

    print("███████╗ ██████╗  ██████╗     ██████╗ ██╗   ██╗")
    print("██╔════╝██╔═══██╗██╔═══██╗    ██╔══██╗╚██╗ ██╔╝")
    print("█████╗  ██║   ██║██║   ██║    ██████╔╝ ╚████╔╝ ")
    print("██╔══╝  ██║   ██║██║   ██║    ██╔═══╝   ╚██╔╝  ")
    print("██║     ╚██████╔╝╚██████╔╝    ██║        ██║   ")
    print("╚═╝      ╚═════╝  ╚═════╝     ╚═╝        ╚═╝   ")
    print("                                               ")

    # p1 = multiprocessing.Process(target=worker_1, args=(5,))
    # p1.start()

    print("The number of CPU is:" + str(multiprocessing.cpu_count()))
    # for p in multiprocessing.active_children():
    #     print("child   p.name:" + p.name + "\tp.id" + str(p.pid))
    # print("END!!!!!!!!!!!!!!!!!")


