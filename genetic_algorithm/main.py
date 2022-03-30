from ui import get_main_parameters, get_function_coeff

if __name__ == '__main__':
    matrix_A, vector_b, c = get_function_coeff()
    dim, int_range, pop_size, cross_prob, mut_prob, iter_num = get_main_parameters()
    print(matrix_A)
    print(vector_b)
    print(c)
    print(dim)
    print(int_range)
    print(pop_size)
    print(cross_prob)
    print(mut_prob)
    print(iter_num)
