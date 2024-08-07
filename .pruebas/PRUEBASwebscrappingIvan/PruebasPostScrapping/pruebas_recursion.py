def quicksort(arr, depth=0):
    indent = "  " * depth  # Para mostrar la profundidad de la recursión
    print(f"{indent}quicksort called with: {arr}")

    if len(arr) <= 1:
        print(f"{indent}Returning: {arr}")
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        print(f"{indent}Pivot: {pivot}")
        print(f"{indent}Left: {left}")
        print(f"{indent}Middle: {middle}")
        print(f"{indent}Right: {right}")

        sorted_left = quicksort(left, depth + 1)
        sorted_right = quicksort(right, depth + 1)

        result = sorted_left + middle + sorted_right
        print(f"{indent}Result: {result}")
        return result


# Ejemplo de uso
arr = [3, 6, 8, 10, 1, 2, 1]
print(quicksort(arr))  # Salida esperada: [1, 1, 2, 3, 6, 8, 10]
