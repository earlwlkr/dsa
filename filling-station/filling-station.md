# FillingStation

Source screenshots:

- [filling-station-1.png](filling-station-1.png)
- [filling-station-2.png](filling-station-2.png)

Calculate the time needed to tank up a queue of cars at a filling station.

## Description

There is a queue of `N` cars waiting at a filling station. There are three fuel dispensers at the station, labeled `X`, `Y`, and `Z`. Each dispenser has some finite amount of fuel in it; at all times the available fuel is clearly displayed on each dispenser.

When a car arrives at the front of the queue, the driver can choose to drive to any dispenser not occupied by another car. Suppose that the fuel demand is `D` liters. The driver must choose a dispenser with at least `D` liters of fuel. If all unoccupied dispensers have less than `D` liters, the driver must wait for another car to finish tanking up. If all dispensers are unoccupied and none has at least `D` liters, the driver is unable to refuel and blocks the queue indefinitely.

If more than one unoccupied dispenser has at least `D` liters, the driver chooses the one labeled with the smallest letter among them.

Each driver may wait before starting to refuel. Calculate the maximum waiting time among all drivers. Assume tanking one liter of fuel takes exactly one second, and moving cars is instantaneous.

Write a function:

```python
def solution(A, X, Y, Z):
    pass
```

that, given an array `A` of `N` integers specifying fuel demands in liters for subsequent cars in the queue, and numbers `X`, `Y`, and `Z` specifying the initial amount of fuel in the respective dispensers, returns the maximum waiting time for a car. If any car is unable to refuel, return `-1`.

## Examples

1. Given `X = 7`, `Y = 11`, `Z = 3`, and `A = [2, 8, 4, 3, 2]`, the function should return `8`.
2. Given `X = 4`, `Y = 0`, `Z = 3`, and `A = [5]`, the function should return `-1`.

## Assumptions

- `N` is an integer within the range `[1..100,000]`.
- Each element of array `A` is an integer within the range `[1..1,000,000,000]`.
- `X`, `Y`, and `Z` are integers within the range `[0..1,000,000,000]`.
