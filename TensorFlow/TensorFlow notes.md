## TensorFlow notes

kaishen, 25 May, 2018

> Why tf creates a computation graph, instead of directly executing the computations?

**Pros:**

+ TF can automatically compute the gradients
+ TF can run the operations in different threads
+ Make it easy to run the same model across different devices
+ Make it easy to view the model, i.e. through TensorBoard

**Cons:**

+ Difficult to debug

> If you create two threas and open a session in each thread, run the same graph. Will the variable be shared or not ?

In **local** TensorFlow, sessions manage variable values. Each session in separate thread will have it own copy of variable, i.e. $w$.

In **distributed** TensorFlow, the stroy changes. Variables are stored in containers managed by the cluster, so if both sessions connect to the same cluster and use the same container, they will shared the same variable for $w$.

 