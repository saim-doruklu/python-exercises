from typing import Iterable


class Signal:
    def __init__(self, input_one: str = None, operation=None, input_two: str = None, value=None):
        self.input_one = input_one
        self.input_two = input_two
        self.operation = operation
        self.value = value


class Gates:

    def generate_system(self, signals: Iterable[str]):
        self.output_input = {}
        self.dependent_gates = {}
        self.resolved_gates = []
        self.gate_values = {}
        for signal in signals:
            output_gate = signal.split("->")[1].strip()

            input_one = None
            input_two = None

            input_params = signal.split("->")[0].strip().split()
            if input_params[0] == "NOT":
                input_one = input_params[1]
                self.output_input[output_gate] = Signal(input_one=input_one, operation=input_params[0])
            elif len(input_params) == 3:
                operation = input_params[1]
                input_one = input_params[0]
                input_two = input_params[2]
                self.output_input[output_gate] = Signal(input_one=input_one, input_two=input_two,
                                                        operation=operation)
            elif str.isnumeric(input_params[0]):
                self.resolved_gates.append([output_gate, int(input_params[0])])
            else:
                input_one = input_params[0]
                self.output_input[output_gate] = Signal(input_one=input_one, operation="EQUAL")

            if input_one is not None and not str.isnumeric(input_one):
                self.dependent_gates.setdefault(input_one, [])
                self.dependent_gates[input_one].append(output_gate)
            if input_two is not None and not str.isnumeric(input_two):
                self.dependent_gates.setdefault(input_two, [])
                self.dependent_gates[input_two].append(output_gate)

    def solve(self):
        index = 0
        while index < len(self.resolved_gates):
            resolved_gate = self.resolved_gates[index][0]
            resolved_value = self.resolved_gates[index][1]
            self.gate_values[resolved_gate] = resolved_value
            dependents_of_this = self.dependent_gates.get(resolved_gate)

            if dependents_of_this is None:
                index += 1
                continue

            for dependent in dependents_of_this:
                dependent_signal = self.output_input[dependent]
                if dependent_signal.operation == "NOT":
                    dependent_value = ~resolved_value
                    self.resolved_gates.append([dependent, dependent_value])
                elif dependent_signal.operation == "LSHIFT":
                    dependent_value = resolved_value << int(dependent_signal.input_two)
                    self.resolved_gates.append([dependent, dependent_value])
                elif dependent_signal.operation == "RSHIFT":
                    dependent_value = resolved_value >> int(dependent_signal.input_two)
                    self.resolved_gates.append([dependent, dependent_value])
                elif dependent_signal.operation == "EQUAL":
                    dependent_value = resolved_value
                    self.resolved_gates.append([dependent, dependent_value])
                else:
                    if dependent_signal.input_one == resolved_gate:
                        other_input = dependent_signal.input_two
                    else:
                        other_input = dependent_signal.input_one

                    if not str.isnumeric(other_input):
                        other_gate_value = self.gate_values.get(other_input)
                    else:
                        other_gate_value = int(other_input)

                    if other_gate_value is not None:
                        if dependent_signal.operation == "AND":
                            dependent_value = resolved_value & other_gate_value
                        elif dependent_signal.operation == "OR":
                            dependent_value = resolved_value | other_gate_value
                        else:
                            raise NotImplementedError("Unknown operation")
                        self.resolved_gates.append([dependent, dependent_value])
            index += 1


if __name__ == '__main__':
    with open('inputs/gates.txt', 'r') as file:
        all_lines = file.readlines()
        gates = Gates()
        gates.generate_system(all_lines)
        gates.solve()
        print(gates.gate_values["a"])
        gates_part_two = Gates()
        gates_part_two.generate_system(all_lines)
        gates_part_two.resolved_gates = [gate for gate in gates_part_two.resolved_gates if gate[0] != "b"] + [
            ["b", 16076]]
        gates_part_two.solve()
        print(gates_part_two.gate_values["a"])
