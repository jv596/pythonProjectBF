from flask import Flask, request, jsonify, url_for, render_template



#NLP Packages
import spacy
from spacy import displacy
from blackstone.displacy_palette import ner_displacy_options
nlp = spacy.load("en_blackstone_proto")

app = Flask(__name__)


@app.route('/home', methods=['GET', 'POST'])
def home():
    return '<h1> Hello, you are on the home page!</h1>'


@app.route('/blackstonetest', methods=['GET', 'POST'])
def blackstonetest():
    #text = """31 As we shall explain in more detail in examining the submission of the Secretary of State (see paras 77 and following), it is the Secretary of State’s case that nothing has been done by Parliament in the European Communities Act 1972 or any other statute to remove the prerogative power of the Crown, in the conduct of the international relations of the UK, to take steps to remove the UK from the EU by giving notice under article 50EU for the UK to withdraw from the EU Treaty and other relevant EU Treaties. The Secretary of State relies in particular on Attorney General v De Keyser’s Royal Hotel Ltd [1920] AC 508 and R v Secretary of State for Foreign and Commonwealth Affairs, Ex p Rees-Mogg [1994] QB 552; he contends that the Crown’s prerogative power to cause the UK to withdraw from the EU by giving notice under article 50EU could only have been removed by primary legislation using express words to that effect, alternatively by legislation which has that effect by necessary implication. The Secretary of State contends that neither the ECA 1972 nor any of the other Acts of Parliament referred to have abrogated this aspect of the Crown’s prerogative, either by express words or by necessary implication.
    #"""

    text = request.form['input']
    doc = nlp(text)
    outputstyle = displacy.render(doc, style="ent", options=ner_displacy_options)
    return (outputstyle)