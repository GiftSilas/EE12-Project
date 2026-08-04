<h1>EE12 Project: Orange Freshness Detection</h1>

<p><em>A Streamlit web app that uses a TensorFlow model to check if an orange is fresh or rotten</em></p>

<p><em>Engineering Project, EE12</em></p>

<hr>

<h2>What It Does</h2>
<p>
Upload a photo of an orange. Before running the freshness check, the app validates that the image
actually shows a round citrus fruit: it uses a pretrained MobileNetV2 model to confirm the object looks
like an orange or lemon, then applies Principal Component Analysis (PCA) on the image's foreground
pixels to reject elongated objects (like eggs) that might otherwise slip past the first check. Once an
image passes both filters, a dedicated model (<code>orange_model.keras</code>) predicts whether the
orange is fresh or rotten, along with a confidence percentage. Predictions that fall in an uncertain
range (roughly 40%–60% confidence) are flagged with a warning instead of a firm result.
</p>

<h3>Classes</h3>
<ul>
  <li>Fresh</li>
  <li>Rotten</li>
  <li>Uncertain Prediction (low-confidence flag)</li>
  <li>Invalid Image (fails the orange/shape validation)</li>
</ul>

<h3>Built With</h3>
<ul>
  <li>Python</li>
  <li>TensorFlow / Keras (MobileNetV2 + custom classifier)</li>
  <li>Streamlit</li>
  <li>NumPy and Pillow</li>
  <li>Scikit-learn (PCA for shape/elongation analysis)</li>
</ul>

<hr>

<h2>How To Set It Up</h2>

<h3>1. Clone the repo</h3>
<pre>
git clone https://github.com/&lt;repo-owner&gt;/EE12-Project.git
cd EE12-Project/EE12
</pre>
<p>
<em>Note: the original source documents disagree on the actual repo owner/URL (different versions
reference different GitHub usernames). Confirm the correct link before sharing this README.</em>
</p>

<h3>2. Install dependencies</h3>
<pre>
pip install -r requirements.txt
</pre>

<h3>3. (Optional) Set up a virtual environment</h3>
<p>Windows:</p>
<pre>
python -m venv venv
venv\Scripts\activate
</pre>
<p>macOS/Linux:</p>
<pre>
python -m venv venv
source venv/bin/activate
</pre>

<h3>4. Train the model (if you want to retrain)</h3>
<p>
Open <code>train_model.ipynb</code> and run the cells in order. It saves the trained model as
<code>orange_model.keras</code>
</p>

<h3>5. Run the app</h3>
<pre>
streamlit run app.py
</pre>
<p>
It opens the local link shown in your terminal (<code>http://localhost:8501</code>) in your browser,
upload an orange photo (.jpg, .jpeg, or .png) and view the freshness prediction
</p>

<hr>

<h2>Known Limitations</h2>
<ul>
  <li>Works best on clear, well-lit photos with the orange visible against a plain or uncluttered background</li>
  <li>The two-step validation (MobileNetV2 + PCA elongation check) reduces but does not eliminate false positives on non-orange or unusually shaped objects</li>
  <li>Accuracy depends heavily on how similar an uploaded photo is to the training data</li>
  <li>Predictions near the 40%–60% confidence range are inherently uncertain and flagged as such rather than given a firm answer</li>
</ul>

<hr>

<h2>Contributors</h2>

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Reg Number</th>
      <th>Github Username</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Silas, Gift Aniekan</td>
      <td>23/EG/EE/035</td>
      <td>GiftAnisilas</td>
    </tr>
    <tr>
      <td>Mfonobong, Emmanuel Christabel</td>
      <td>23/EG/EE/025</td>
      <td>Queencrystal01</td>
    </tr>
    <tr>
      <td>—</td>
      <td>23/EG/EE/075</td>
      <td>—</td>
    </tr>
    <tr>
      <td>—</td>
      <td>23/EG/EE/115</td>
      <td>—</td>
    </tr>
    <tr>
      <td>Chidiebere, Oliver Emmanuel</td>
      <td>23/EG/EE/015</td>
      <td>oliver-creator1</td>
    </tr>
    <tr>
      <td>Mfon, Godswill</td>
      <td>23/EG/EE/045</td>
      <td>mfongodswill68-cmd</td>
    </tr>
    <tr>
      <td>Sema, Effiong Kelvin</td>
      <td>23/EG/EE/105</td>
      <td>kelzzz-gif</td>
    </tr>
    <tr>
      <td>—</td>
      <td>23/EG/EE/065</td>
      <td>—</td>
    </tr>
  </tbody>
</table>
<hr>

<h2>Contributors' Comments</h2>

<h3>Gift Silas</h3>
<p>
The Citrus Quality Evaluation tool verifies uploaded oranges using MobileNetV2 for fruit identification
and PCA-based shape analysis to screen out oblong objects, before a specialized network assesses
whether the fruit is fresh or spoiled
</p>

<h3>23/EG/EE/115</h3>
<p>
The Citrus Quality Evaluation tool checks whether an uploaded orange is sound or spoiled, using
MobileNetV2 to confirm the image shows a citrus fruit and PCA-based shape analysis to filter out
oblong objects like eggs, before a dedicated network judges the fruit's condition
</p>

<h3>oliver-creator1</h3>
<p>
This project lets a user upload an orange photo and get a freshness read, after checking the image
actually looks like an orange and isn't an oddly shaped object. It's a class project with room to grow —
more diverse training data, better background handling, and cloud deployment are all listed as future
improvements rather than finished features
</p>

<h3>Mfon, Godswill</h3>
<p>
This mini project was built to demonstrate the practical application of concepts from GET 324, with a
focus on structured project planning, implementation, and documentation as much as the technical result
itself
</p>

<h3>23/EG/EE/065</h3>
<p>
The project classifies oranges as fresh or rotten and uses MobileNetV2 pre-validation together with a
PCA-based elongation check to cut down on false positives from non-orange or non-round objects
</p>

<h3>23/EG/EE/075</h3>
<p>
The Citrus Quality Evaluation tool uses a multi-stage vision pipeline verifying image type, filtering
out non-spherical shapes, and detecting spoil to automatically grade uploaded oranges
</p>

<hr>

<h2>License</h2>
<p>Academic project for the GET 324 Engineering course</p>
