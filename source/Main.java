package source;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
import java.awt.BorderLayout;
import java.awt.Dimension;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import javax.swing.JLabel;

public class Main implements ActionListener {

    JFrame frame;
    JPanel panelMain, panelIRP, panelTop;
    JButton buttonIRP, buttonCSM;
    JButton buttonTechAndConnectionTypes, buttonDeliveryChannels, buttonProductsAndTechnologyServices, buttonOrganizationalCharacteristics, buttonExternalThreats;
    JButton labelTop;

    public Main() {
      
        // buttons of the home page
        buttonIRP = new JButton("Inherent Risk Profile");
        buttonIRP.setBounds(50, 50, 200, 50);  ////////////////
        buttonIRP.addActionListener(this);
        buttonCSM = new JButton("Cybersecurity Maturity");
        buttonCSM.setBounds(50, 100, 200, 50);     ////////////////
        buttonCSM.addActionListener(this);

        // buttons of the IRP page
        buttonTechAndConnectionTypes = new JButton("Technologies and Connections");
        buttonDeliveryChannels = new JButton("Delivery Channels");
        buttonDeliveryChannels.setBounds(50,50,200,50);
        buttonProductsAndTechnologyServices = new JButton("Products and Technologies");
        buttonOrganizationalCharacteristics = new JButton("Organizational Characteristics");
        buttonExternalThreats = new JButton("External Threats");

        // main panel of the home page
        panelMain = new JPanel();
        panelMain.setLayout(null);
        panelMain.add(buttonIRP);
        panelMain.add(buttonCSM);

        // panel of the IRP page
        panelIRP = new JPanel();  
        panelIRP.add(buttonTechAndConnectionTypes);
        panelIRP.add(buttonDeliveryChannels);
        panelIRP.add(buttonProductsAndTechnologyServices);
        panelIRP.add(buttonOrganizationalCharacteristics);
        panelIRP.add(buttonExternalThreats);

        // top panel
        panelTop = new JPanel();
        panelTop.setSize(500,400);
        labelTop = new JButton("Test");
        labelTop.addActionListener(this);
        panelTop.add(labelTop);
        panelMain.add(panelTop);

        // main frame
        frame = new JFrame();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setTitle("Home");
        frame.setSize(new Dimension(600,400));
        frame.setVisible(true);
        frame.add(panelMain, BorderLayout.CENTER);
        frame.setContentPane(panelMain);
    }

    public static void main(String[] args){

        new Main();
        IRP test = new IRP();
        
        for (String key : test.questions.keySet()) {
            for (int i = 0; i < test.questions.get(key).length; i++) {
                System.out.println(key + " : " + test.questions.get(key)[i]);
            }
        }

        test.getAnswers();
        for (String key : test.answers.keySet()) {
            System.out.println(key + " : " + test.answers.get(key));
            
        }
    }

    @Override
    public void actionPerformed(ActionEvent e) {

        // IRP button pressed
        if (e.getSource() == buttonIRP) {
            frame.setContentPane(panelIRP);
            frame.repaint();
            frame.revalidate();
        }

        if (e.getSource() == labelTop) {
            frame.setContentPane(panelIRP);
            frame.repaint();
            frame.revalidate();
        }
    }
}