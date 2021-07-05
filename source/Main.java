package source;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
import java.awt.BorderLayout;
import java.awt.Dimension;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class Main implements ActionListener {

    JFrame frame;
    JPanel panel, panelIRP;
    JButton buttonIRP, buttonCSM;
    JButton buttonTechAndConnectionTypes, buttonDeliveryChannels, buttonProductsAndTechnologyServices, buttonOrganizationalCharacteristics, buttonExternalThreats;

    public Main() {

        // main frame
        frame = new JFrame();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setTitle("Home");
        frame.setSize(new Dimension(600,400));
        frame.setVisible(true);

        // main panel of the home page
        panel = new JPanel();
        panel.setLayout(null);
        panel.setSize(frame.getSize());
        frame.setContentPane(panel);

        // panel of the IRP page
        panelIRP = new JPanel();

        // buttons of the home page
        buttonIRP = new JButton("Inherent Risk Profile");
        buttonCSM = new JButton("Cybersecurity Maturity");
        buttonIRP.setBounds(panel.getWidth() / 3, panel.getHeight() / 3, 200, 50);  ////////////////
        buttonCSM.setBounds(buttonIRP.getX(), buttonIRP.getY() + 100, 200, 50);     ////////////////
        buttonIRP.addActionListener(this);
        buttonCSM.addActionListener(this);

        // buttons of the IRP page
        buttonDeliveryChannels = new JButton("Delivery Channels");
        buttonDeliveryChannels.setBounds(50,50,200,50);
        buttonTechAndConnectionTypes = new JButton("Technologies and Connections");
        buttonProductsAndTechnologyServices = new JButton("Products and Technologies");
        buttonOrganizationalCharacteristics = new JButton("Organizational Characteristics");
        buttonExternalThreats = new JButton("External Threats");

        panel.add(buttonIRP);
        panel.add(buttonCSM); 
        panelIRP.add(buttonDeliveryChannels);
        panelIRP.add(buttonTechAndConnectionTypes);
        panelIRP.add(buttonProductsAndTechnologyServices);
        panelIRP.add(buttonOrganizationalCharacteristics);
        panelIRP.add(buttonExternalThreats);
        frame.add(panel, BorderLayout.CENTER);        
    }

    public static void main(String[] args){

        new Main();
        IRP test = new IRP();
        
        for (String key : test.questions.keySet()) {
            for (int i = 0; i < test.questions.get(key).length; i++) {
                System.out.println(key + " : " + test.questions.get(key)[i]);
            }
        }

        test.fillAnswers();
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

    }
}