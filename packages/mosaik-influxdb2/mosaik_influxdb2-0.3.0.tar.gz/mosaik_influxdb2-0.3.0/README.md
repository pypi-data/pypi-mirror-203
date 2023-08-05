# mosaik-influxdb2

This package contains an adapter to write data from a mosaik simulation into an
InfluxDB 2 database.

## Installation

This package is on pypi, so you can install it using pip:

```sh
pip install mosaik-influxdb2
```

## Usage

To use the simulator, first add it to your `sim_config`:

```python
sim_config = {
    "InfluxWriter": {"python": "mosaik.components.influxdb2.writer:Simulator"},
    # ...
}
```

Next, you need to start the simulator. Here, you have two choices to make:

1. The simulator can run both in time-based mode with a fixed step size or in
   event-based mode without a step size. You can choose the time-based mode by giving
   the parameter `step_size` when starting the simulator. If you give `step_size=None`
   (or don’t specify anything), the simulator will use the event-based mode.
2. You can either supply a start date (as a string parseable by Python’s `datetime`
   module) which will be combined with the (mosaik) time and time resolution to
   calculate each step’s time, or you can supply the time for each step on the
   `local_time` attribute (again, as a string). If you give both, the value on the
   `local_time` attribute will take precedence.

So one possible invocation would be

```python
influx_sim = world.start("InfluxWriter",
    step_size=900,
    start_date="2022-01-01 00:00:00Z",
)
```

to start the simulator in time-based mode with a step size of 900 and times based on
the given start date. You can leave off either argument with the effects described
above.

Finally, the model needs to be started with your Influx credentials:

```python
influx = influx_sim.Database(
    url="http://localhost:8086",
    org='.',
    bucket='my_bucket',
    token='secret_token',
    measurement='experiment_0001'
)
```

We recommend setting a new value for the measurement on each simulation run. (For
example, you can use the start time of your simulation or a random UUID.)

Afterwards, you can define `world.connect(other_entity, influx, attrs)` as you like.

The simulator supports only one instance of the Database model. If you want to connect
to several databases, you will need to start several instances of the simulator as well.
