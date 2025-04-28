---
tags: 
aliases: 
category: 
phase: 
topic: 
filename:
---
[10 Design Patterns Explained in 10 Minutes](https://www.youtube.com/watch?v=tv-_1er1mWI)

# Software Design Patterns

## What Are Software Design Patterns?

Software design patterns provide reusable solutions to common software design problems. They help standardize approaches, making code easier to understand, maintain, and extend. The influential book _Design Patterns_ by the "Gang of Four" categorizes design patterns into three types:

- **Creational Patterns**: Handle object creation mechanisms.
- **Structural Patterns**: Define how objects and components relate.
- **Behavioral Patterns**: Govern object communication and workflows.

Using design patterns effectively can improve code quality, but excessive or incorrect use may introduce unnecessary complexity.

## Key Software Design Patterns

### Singleton Pattern

The **Singleton pattern** ensures that only one instance of a class exists and provides a global point of access.

Use Cases: [[Database]] connections, Logging services, Global configurations
#### Example (JavaScript):

```javascript
class Singleton {
  constructor() {
    if (!Singleton.instance) {
      Singleton.instance = this;
    }
    return Singleton.instance;
  }
}
const instance1 = new Singleton();
const instance2 = new Singleton();
console.log(instance1 === instance2); // true
```

### Prototype Pattern

The **Prototype pattern** allows new objects to be created by cloning an existing object rather than instantiating a new class.

Use Cases: Performance optimization, Object cloning

#### Example (JavaScript):

```javascript
const carPrototype = {
  start: function () {
    console.log("Engine started!");
  }
};
const myCar = Object.create(carPrototype);
myCar.start(); // Engine started!
```

### Builder Pattern

The **Builder pattern** simplifies object creation when multiple configuration options exist.

Use Cases: Constructing complex objects, UI component creation

#### Example (JavaScript):

```javascript
class CarBuilder {
  constructor() {
    this.car = {};
  }
  setColor(color) {
    this.car.color = color;
    return this;
  }
  setWheels(wheels) {
    this.car.wheels = wheels;
    return this;
  }
  build() {
    return this.car;
  }
}
const myCar = new CarBuilder().setColor("red").setWheels(4).build();
console.log(myCar);
```

### Factory Pattern

The **Factory pattern** encapsulates object creation logic, making code more modular and easier to extend.

Use Cases: Dependency injection, Platform-specific object creation

#### Example (JavaScript):

```javascript
class CarFactory {
  static createCar(type) {
    const carTypes = {
      sedan: { type: "sedan", doors: 4 },
      coupe: { type: "coupe", doors: 2 },
    };
    return carTypes[type] || null;
  }
}
const myCar = CarFactory.createCar("sedan");
console.log(myCar);
```

### Facade Pattern

The **Facade pattern** provides a simplified interface to a complex system.

Use Cases: Simplifying APIs, Reducing dependencies

#### Example (JavaScript):

```javascript
class Computer {
  start() { console.log("Computer starting..."); }
  shutdown() { console.log("Computer shutting down..."); }
}
class ComputerFacade {
  constructor() {
    this.computer = new Computer();
  }
  turnOn() {
    this.computer.start();
  }
  turnOff() {
    this.computer.shutdown();
  }
}
const myComputer = new ComputerFacade();
myComputer.turnOn();
```

### Proxy Pattern

The **Proxy pattern** acts as an intermediary to control access to an object.

Use Cases: Lazy loading, [[Data Security]] proxies

#### Example (JavaScript):

```javascript
class RealImage {
  constructor(filename) {
    this.filename = filename;
  }
  display() {
    console.log("Displaying " + this.filename);
  }
}
class ProxyImage {
  constructor(filename) {
    this.realImage = null;
    this.filename = filename;
  }
  display() {
    if (!this.realImage) {
      this.realImage = new RealImage(this.filename);
    }
    this.realImage.display();
  }
}
const image = new ProxyImage("test.jpg");
image.display();
```

### Iterator Pattern

The **Iterator pattern** provides a way to access elements of a collection sequentially without exposing its internal structure.

Use Cases: Collection traversal, Data processing

#### Example (JavaScript):

```javascript
class Iterator {
  constructor(items) {
    this.items = items;
    this.index = 0;
  }
  next() {
    return this.index < this.items.length ? { value: this.items[this.index++], done: false } : { done: true };
  }
}
const iterator = new Iterator(["a", "b", "c"]);
console.log(iterator.next());
console.log(iterator.next());
console.log(iterator.next());
```

### Observer Pattern

The **Observer pattern** enables a one-to-many dependency between objects, ensuring changes to one object are reflected in its dependents.

Use Cases: Event handling, Reactive programming

#### Example (JavaScript):

```javascript
class Subject {
  constructor() {
    this.observers = [];
  }
  subscribe(observer) {
    this.observers.push(observer);
  }
  notify(data) {
    this.observers.forEach(observer => observer.update(data));
  }
}
class Observer {
  update(data) {
    console.log("Received update: " + data);
  }
}
const subject = new Subject();
const observer1 = new Observer();
subject.subscribe(observer1);
subject.notify("Hello World");
```

### Mediator Pattern

The **Mediator pattern** centralizes communication between objects to reduce dependencies.

Use Cases: Chat applications, Workflow coordination

#### Example (JavaScript):

```javascript
class Mediator {
  constructor() {
    this.participants = [];
  }
  register(participant) {
    this.participants.push(participant);
  }
  send(message, sender) {
    this.participants.forEach(participant => {
      if (participant !== sender) {
        participant.receive(message);
      }
    });
  }
}
class Participant {
  constructor(name, mediator) {
    this.name = name;
    this.mediator = mediator;
    mediator.register(this);
  }
  send(message) {
    this.mediator.send(message, this);
  }
  receive(message) {
    console.log(this.name + " received: " + message);
  }
}
const mediator = new Mediator();
const p1 = new Participant("Alice", mediator);
p1.send("Hello");
```
