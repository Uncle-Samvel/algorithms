def generate_expression(result: list, total: int, current_num: int = 1, current_expression: str = '0'):
    if current_num == 10:
        if eval(current_expression) == total:
            result.append(current_expression)
        return

    generate_expression(result, total, current_num + 1, str(current_num) + '+' + current_expression)
    generate_expression(result, total, current_num + 1, str(current_num) + '-' + current_expression)
    generate_expression(result, total, current_num + 1, str(current_num) + current_expression)


# число которое необходимо получить
required_number = 200
answer = list()
generate_expression(result=answer, total=required_number)

print(f'only {len(answer)} expressions:')
for expression in answer:
    print(f'{expression} = {required_number}')
